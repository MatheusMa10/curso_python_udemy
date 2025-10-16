velocidade = 61
local_carro = 101

radar = 60
local = 100
radar_range = 1

vai_ser_multado = velocidade > radar
localidade_do_carro_comparado_com_radar = local_carro >= (local - radar_range) and local_carro <= (local + radar_range)

if vai_ser_multado:
    print('Velocidade do carro passou do radar')

if localidade_do_carro_comparado_com_radar:
    print('carro passou radar')

if vai_ser_multado and localidade_do_carro_comparado_com_radar:
    print('foi multado')