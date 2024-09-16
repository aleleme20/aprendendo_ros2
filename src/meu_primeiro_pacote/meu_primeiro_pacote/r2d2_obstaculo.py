import rclpy
import tf_transformations
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3

from rclpy.qos import QoSProfile, QoSReliabilityPolicy

import math
from math import *
import numpy
import time 

class R2D2(Node):

    def __init__(self):
        super().__init__('R2D2')
        self.get_logger().debug ('Definido o nome do nó para "R2D2"')

        qos_profile = QoSProfile(depth=10, reliability = QoSReliabilityPolicy.BEST_EFFORT)

        self.get_logger().debug ('Definindo o subscriber do laser: "/scan"')
        self.laser = None
        self.create_subscription(LaserScan, '/scan', self.listener_callback_laser, qos_profile)

        self.get_logger().debug ('Definindo o subscriber do laser: "/odom"')
        self.pose = None
        self.create_subscription(Odometry, '/odom', self.listener_callback_odom, qos_profile)

        self.get_logger().debug ('Definindo o publisher de controle do robo: "/cmd_Vel"')
        self.pub_cmd_vel = self.create_publisher(Twist, '/cmd_vel', 10)

        self.estado_robo = 0
        self.wait(0.5)
        self.d = 0.0

    def wait(self, max_seconds):
        start = time.time()
        count = 0
        while count < max_seconds:
            count = time.time() - start            
            rclpy.spin_once(self)

    def listener_callback_laser(self, msg):
        self.laser = msg.ranges
       
    def listener_callback_odom(self, msg):
        self.pose = msg.pose.pose

    def distancia_robo_objetivo(self): #função que calcula a distância e o robô e o (9,9)
        obj = [9,9]
        p_robo = [self.pose.position.x, self.pose.position.y]
        self.d = math.dist(obj, p_robo) #distância
        
        

    def run(self):

       
        self.get_logger().debug ('Executando uma iteração do loop de processamento de mensagens.')
        rclpy.spin_once(self)

        self.get_logger().debug ('Definindo mensagens de controde do robô.')
        self.ir_para_frente = Twist(linear=Vector3(x= 0.5,y=0.0,z=0.0),angular=Vector3(x=0.0,y=0.0,z= 0.0))
        self.parar          = Twist(linear=Vector3(x= 0.0,y=0.0,z=0.0),angular=Vector3(x=0.0,y=0.0,z= 0.0))

        self.get_logger().info ('Ordenando o robô: "ir para a frente"')
        self.pub_cmd_vel.publish(self.ir_para_frente)
        rclpy.spin_once(self)
        

        self.get_logger().info ('Entrando no loop princial do nó.')
        while(rclpy.ok):
            
            self.pose.orientation #orientation
            self.pose.position #posicao
            _, _, yaw = tf_transformations.euler_from_quaternion([self.pose.orientation.x, self.pose.orientation.y, self.pose.orientation.z, self.pose.orientation.w]) #aqui so precisa usar o yaw

            rclpy.spin_once(self)

            #distancia_direita = numpy.array(self.laser[0:10]).mean()
            self.get_logger().debug ('Atualizando as distancias lidas pelo laser.')
            self.distancia_direita   = min((self.laser[  0: 80])) # -90 a -10 graus
            self.distancia_frente    = min((self.laser[ 80:100])) # -10 a  10 graus
            self.distancia_esquerda  = min((self.laser[100:180])) #  10 a  90 graus

            cmd = Twist()

            if(self.estado_robo == 0): #estado 0 = virar orientação para (9,9)
        
                #cmd.linear.x = 0.00
                cmd.angular.z = 0.5
                self.pub_cmd_vel.publish(cmd)
                self.get_logger().info ("VIRANDO")

                if(yaw >= pi/4):
                    cmd.angular.z = 0.00
                    self.pub_cmd_vel.publish(cmd)
                    self.estado_robo = 1 #estado 1 = andar para de frente
                    self.get_logger().info ("PAROU DE VIRAR")

            elif(self.estado_robo == 1):
                if (self.distancia_frente >= self.d):
                    cmd.linear.x = 0.5
                    self.pub_cmd_vel.publish(cmd)
                    self.get_logger().info ("INDO PARA FRENTE")
                    if(self.d == 0):
                        cmd.linear.x = 0.0
                        self.pub_cmd_vel.publish(cmd)
                        self.get_logger().info ("OBJETIVO ALCANCADO")
                else:
                    self.estado_robo = 2
            
            elif(self.estado_robo == 2):
                cmd.angular.z = 0.1
                self.pub_cmd_vel.publish(cmd)
                if(self.distancia_frente > self.distancia_direita and self.distancia_frente > self.distancia_esquerda):
                    cmd.angular.z = 0.0
                    self.pub_cmd_vel.publish(cmd)



            self.get_logger().debug ("Distância para o obstáculo" + str(self.distancia_frente))
                
                  
        self.get_logger().info ('Ordenando o robô: "parar"')
        self.pub_cmd_vel.publish(self.parar)
        rclpy.spin_once(self)


    # Destrutor do nó
    def __del__(self):
        self.get_logger().info('Finalizando o nó! Tchau, tchau...')


# Função principal
def main(args=None):
    rclpy.init(args=args)
    node = R2D2()
    try:
        node.run()
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass
   
if __name__ == '__main__':
    main()  
