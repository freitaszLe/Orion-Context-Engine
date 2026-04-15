import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LogExecucao } from '../../models/chat.model';

@Component({
  selector: 'app-execution-log',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './execution-log.component.html',
  styleUrls: ['./execution-log.component.scss']
})
export class ExecutionLogComponent {
  @Input() logs: LogExecucao[] = [];
  logAberto = true;

  alternarLog(): void {
    this.logAberto = !this.logAberto;
  }
}