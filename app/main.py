import turtle


def desenhar_petala(t, tamanho):
    t.begin_fill()
    t.circle(tamanho, 60)
    t.left(120)
    t.circle(tamanho, 60)
    t.left(120)
    t.end_fill()


def desenhar_camadas_de_petalas(t, camadas=4):
    for camada in range(camadas):
        t.color("dark red", "red")
        tamanho = 160 - camada * 15
        num_petalas = 9  
        for i in range(num_petalas):
            angulo = 0 + (i * (100 / (num_petalas - 1)))
            t.up()
            t.setheading(angulo + 5)
            t.down()
            desenhar_petala(t, tamanho)


def desenhar_calice(t):
    t.color("dark green", "dark green")
    t.begin_fill()
    for _ in range(5): 
        t.forward(8)
        t.left(90)
        t.forward(15)
        t.right(60)
    t.end_fill()


def desenhar_folha(t, tamanho):
    t.color("dark green", "#2e8b57")
    t.begin_fill()
    t.setheading(-90)
    
    t.left(30)
    t.forward(tamanho*0.7)
    t.circle(tamanho*0.4, 60)
    t.forward(tamanho*0.5)
    t.circle(tamanho*0.2, 60)
    t.forward(tamanho*0.3)
    t.left(120)
    t.forward(tamanho*0.3)
    t.circle(tamanho*0.2, 60)
    t.forward(tamanho*0.5)
    t.circle(tamanho*0.4, 60)
    t.forward(tamanho*0.7)
    t.end_fill()
    t.right(30)


def desenhar_caule(t):
    t.color("dark green", "green")
    t.width(8)
    t.forward(20)
    desenhar_folha(t, 50)
    t.forward(60)


def escrever_texto(t):
    t.up()
    t.goto(0, -240)
    t.color("black")
    t.write("25 de Abril Sempre!", align="center", font=("Arial", 24, "bold"))
    t.goto(0, -260)
    t.color("gray")
    t.write("ISCTE - Escola de Tecnologias Digitais Aplicadas de Sintra", align="center", font=("Arial", 14))


def main():
    tela = turtle.Screen()
    tela.bgcolor("white")
    tela.title("Cravo - 25 de Abril")

    t = turtle.Turtle()
    t.speed(0)
    t.up()
    t.goto(0, 0)
    t.down()

    desenhar_camadas_de_petalas(t)
    
    t.up()
    t.goto(-30, 10)
    t.setheading(240)
    t.down()
    desenhar_calice(t)
    
    t.up()
    t.goto(0, -15)
    t.setheading(-90) 
    t.down()
    desenhar_caule(t)

    escrever_texto(t)
    t.hideturtle()
    tela.exitonclick()


if __name__ == "__main__":
    main()