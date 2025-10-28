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

quando usar cada um:

recall: falso negativo é caro:
            diagnosticar alguem errado com cancer por exemplo
            nesse caso o falar que nao tem (e ter) sai mt caro

precisao: falso positivo sai caro:
            afirmar que x pessoa esta relacionada com fraude bancarias
            (e nao estar) sai mt caro pro banco e pessoa

f1 score: quando tem uma chance de 0 - 1 para avaliar algo
            avaliar se um email é spam, tem uma chance, de 0.5 por exemplo
            nesse caso tu escolhe o churn e diz, se de acordo com o threshold de0.5 é churn ou
            nao,

roc auc: o modelo escolhe sem que tu precise de um threshold ainda

r²: quanto mais proximo de 1 melhor
            o r² é basicamente quao bem o modelo esta explicando um target de acordo com
            as features, oque fazer para melhor?
                checar overfitting, se tiver - regulariza ou early stopping
                melhorar as features,
                aumentar base de dados
                geralmente ocorre por isso ai