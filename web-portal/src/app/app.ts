import { Component, ViewChild, ElementRef, AfterViewChecked } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class AppComponent implements AfterViewChecked {
  @ViewChild('scrollMe') private myScrollContainer!: ElementRef;

  mensagens: { texto: string, autor: 'usuario' | 'ia' }[] = [
    { texto: 'Olá! Sou o assistente inteligente do X-SIG. Digite o ID de um bolsista para eu consultar.', autor: 'ia' }
  ];

  novaMensagem: string = '';
  carregando: boolean = false; // Controla a animação de "digitando..."

  constructor(private http: HttpClient) {}

  ngAfterViewChecked() {
    this.rolarParaBaixo();
  }

  rolarParaBaixo(): void {
    try {
      this.myScrollContainer.nativeElement.scrollTop = this.myScrollContainer.nativeElement.scrollHeight;
    } catch(err) { }
  }

  enviarMensagem() {
    if (this.novaMensagem.trim() === '' || this.carregando) return;

    let textoDigitado = this.novaMensagem;
    this.mensagens.push({ texto: textoDigitado, autor: 'usuario' });
    this.novaMensagem = '';
    this.carregando = true; // Liga a animação de pensar

    this.http.post<any>('http://localhost:8000/api/chat', { texto: textoDigitado })
      .subscribe({
        next: (resposta) => {
          this.mensagens.push({ texto: resposta.mensagem, autor: 'ia' });
          this.carregando = false; // Desliga a animação
        },
        error: (erro) => {
          this.mensagens.push({ texto: 'Ops! O servidor parece estar desligado.', autor: 'ia' });
          this.carregando = false;
        }
      });
  }

  // Pega o texto do Gemini e transforma **texto** em negrito e \n em quebra de linha
  formatarTexto(texto: string): string {
    let formatado = texto.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    return formatado.replace(/\n/g, '<br>');
  }
}
