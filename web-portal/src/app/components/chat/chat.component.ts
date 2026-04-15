import {
  Component,
  Input,
  Output,
  EventEmitter,
  ElementRef,
  ViewChild,
  AfterViewChecked
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Mensagem } from '../../models/chat.model';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements AfterViewChecked {
  @Input() mensagens: Mensagem[] = [];
  @Input() carregando = false;
  @Output() enviar = new EventEmitter<string>();

  novaMensagem = '';

  @ViewChild('chatScroll')
  private chatScrollContainer!: ElementRef<HTMLDivElement>;

  ngAfterViewChecked(): void {
    this.rolarParaBaixo();
  }

  private rolarParaBaixo(): void {
    try {
      const container = this.chatScrollContainer.nativeElement;
      container.scrollTop = container.scrollHeight;
    } catch {}
  }

  enviarMensagemLocal(): void {
    const texto = this.novaMensagem.trim();

    if (!texto || this.carregando) {
      return;
    }

    this.enviar.emit(texto);
    this.novaMensagem = '';
  }
}