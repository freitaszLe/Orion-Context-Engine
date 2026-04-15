import { SafeHtml } from '@angular/platform-browser';

export interface Mensagem {
  role: 'user' | 'orion';
  texto: string | SafeHtml;
}

export interface LogExecucao {
  hora: string;
  titulo: string;
  detalhe: string;
  tipo: 'info' | 'success' | 'error';
}