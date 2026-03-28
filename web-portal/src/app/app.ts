
import { Component, ElementRef, ViewChild, AfterViewChecked } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {HttpClient, HttpClientModule} from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.html',   // <-- Tire o ".component"
  styleUrls: ['./app.scss']    // <-- Tire o ".component"
})
export class AppComponent implements AfterViewChecked {
  @ViewChild('chatScroll') private chatScrollContainer!: ElementRef;

  // Variável que o HTML está reclamando
  mensagens: { role: string, texto: string }[] = [
    { role: 'orion', texto: 'Olá! Eu sou o Orion Context Engine, o assistente virtual inteligente do sistema X-SIG da FAPEMAT. Como posso te ajudar hoje?' }
  ];

  // Variáveis adicionais necessárias
  novaMensagem: string = '';
  carregando: boolean = false;

  constructor(private http: HttpClient) {}

  // Garante que a tela role para baixo sempre que uma nova mensagem chegar
  ngAfterViewChecked() {
    this.rolarParaBaixo();
  }

  rolarParaBaixo(): void {
    try {
      this.chatScrollContainer.nativeElement.scrollTop = this.chatScrollContainer.nativeElement.scrollHeight;
    } catch(err) { }
  }

  // Função que o HTML está reclamando
  enviarMensagem() {
    if (!this.novaMensagem.trim() || this.carregando) return;

    const textoUsuario = this.novaMensagem;
    // 1. Coloca a mensagem do usuário na tela
    this.mensagens.push({ role: 'user', texto: textoUsuario });
    this.novaMensagem = '';
    this.carregando = true;

    // 2. Bate na porta 8002 onde está a nossa AI Bridge (FastAPI)
    this.http.post<{mensagem: string}>('http://localhost:8002/api/chat', { texto: textoUsuario })
      .subscribe({
        next: (res) => {
          this.mensagens.push({ role: 'orion', texto: res.mensagem });
          this.carregando = false;
        },
        error: (err) => {
          console.error(err);
          this.mensagens.push({ role: 'orion', texto: 'Desculpe, a conexão com o núcleo do Llama 3.1 falhou. Verifique se o servidor FastAPI está rodando na porta 8002.' });
          this.carregando = false;
        }
      });
  }
}
