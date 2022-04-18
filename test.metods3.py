from robot_control_class import RobotControl

robotcontrol = RobotControl(robot_name="summit")   #objetodaclasseRobôSummit

robotcontrol.move_straight_time("forward", 0.5, 5)
robotcontrol.turn("clockwise",0.5,10)

#utilizamos do objeto da classe para chamar os métodos, cada método com seus parâmetros.

# O primeiro método move o Robô(CARRO) - para a frente "forward", a uma velocidade de 0.5 metros por segundo "0.5", por 5 segundos.
# O segundo método, gira o Robô(CARRO) - no sentindo horário "clockwise", a uma velocidade de 0.5 metros por segundo "0.5", por 10 segundos.
