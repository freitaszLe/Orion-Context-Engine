import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OrionService {
  private readonly API_URL = 'http://localhost:8002/api/chat';

  constructor(private http: HttpClient) {}

  enviarMensagem(texto: string): Observable<{ mensagem: string }> {
    return this.http.post<{ mensagem: string }>(this.API_URL, { texto });
  }
}