import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DomSanitizer } from '@angular/platform-browser';
import { OrionService } from './services/orion.service';
import { Mensagem, LogExecucao } from './models/chat.model';
import { ChatComponent } from './components/chat/chat.component';
import { ExecutionLogComponent } from './components/execution-log/execution-log.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ChatComponent, ExecutionLogComponent],
  templateUrl: './app.html',
  styleUrls: ['./app.scss']
})
export class AppComponent {
  mensagens: Mensagem[] = [
    { role: 'orion', texto: 'Olá! Eu sou o Orion Context Engine. Como posso ajudar?' }
  ];
  logsExecucao: LogExecucao[] = [];
  carregando = false;

  constructor(
    private orionService: OrionService, 
    private sanitizer: DomSanitizer
  ) {}

  private formatarResposta(textoBruto: string) {
    let formatado = textoBruto.replace(/\n/g, '<br>');
    formatado = formatado.replace(/\*\s/g, '• ');
    return this.sanitizer.bypassSecurityTrustHtml(formatado);
  }

  private adicionarLog(titulo: string, detalhe: string, tipo: LogExecucao['tipo'] = 'info') {
    this.logsExecucao.unshift({ 
      hora: new Date().toLocaleTimeString(), 
      titulo, detalhe, tipo 
    });
  }

  processarComando(textoUsuario: string) {
    this.mensagens.push({ role: 'user', texto: textoUsuario });
    this.carregando = true;

    this.adicionarLog('Usuário', textoUsuario);
    this.adicionarLog('Orquestrador', 'Enviando intenção para o Llama 3.1...');

    this.orionService.enviarMensagem(textoUsuario).subscribe({
      next: (res) => {
        this.mensagens.push({ role: 'orion', texto: this.formatarResposta(res.mensagem) });
        this.adicionarLog('IA Core', 'Processamento concluído.', 'success');
        this.carregando = false;
      },
      error: () => {
        this.adicionarLog('Falha', 'Erro de conexão.', 'error');
        this.mensagens.push({ role: 'orion', texto: 'Conexão falhou.' });
        this.carregando = false;
      }
    });
  }
}