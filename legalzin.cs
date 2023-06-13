using System;

public class Carros {
    protected int rodas;
    protected int portas;
    protected string cor;
    public void Carros(string cor) {
        rodas = 4;
        portas = 4;
        this.cor = cor;
    }
    public void setRodas(int rodas) {
        this.rodas = rodas;
    }
    public void setPortas(int portas) {
        this.portas = portas;
    }
}

public class CarroCombate:Carros {
    protected int armas;
    public int balas;
    protected int grossuraPneu;
    public void CarroCombate(int armas, int grossuraPneu) {
        if (armas < 4 && armas > 0) {
            this.armas = armas;
        } else {
            if (armas > 4) {
                this.armas = 4;
            } else {
                this.armas = 0;
            }
        }
    }
    public void atirar() {
        Console.WriteLine("Pei pei");
        balas -= 1;
        Console.WriteLine("Voce tem {0} balas", balas);
        
    }
}

public class Jogador {
    static void Main() {
        CarroCombate carro = new CarroCombate(2, 10);
        carro.atirar();
    }
}