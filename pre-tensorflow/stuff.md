acuracia:
    basicamente: numero de certos/numero de errado

precisao:
    de acordo com oq eu """chutei""" quantos estavam certo? (o foco é dentro de quantos o modelo acertou)
        TruePositives/TruePositives + FalsePositives = x

recall:
    de acordo com TODOS, quantos eu acertei? (o foco é o geral)
        TruePositives/TruePositives + FalseNegatives = y

f1:
    F1 é útil quando você quer balancear acerto dentro da bolha (precision) e cobertura geral (recall).
        basicamente o equilibrio entre o recall e precisao
            2 x (Precisao x Recall/Precisao + Recall) 

