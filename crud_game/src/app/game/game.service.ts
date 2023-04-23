import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { GamesResponse,ResponseCreateGame,CreateGame,GameResponse } from "./game.model";

@Injectable({
  providedIn: 'root'
})
export class GameService {
  private apiUrl = 'http://localhost:5000';
  constructor(private http: HttpClient) { }
  getAll(): Observable<GamesResponse> {
    return this.http.get<GamesResponse>(`${this.apiUrl}/all?search=games`);
  }
  createGame(request: CreateGame): Observable<ResponseCreateGame>{
    return this.http.post<ResponseCreateGame>(`${this.apiUrl}/add?search=games`,request);
  }
  getGame(id:string){
    return this.http.get<GameResponse>(`${this.apiUrl}/find?search=games&id=${id}`);
  }
  updateGame(id:string,request:CreateGame){
    return this.http.post<ResponseCreateGame>(`${this.apiUrl}/update?search=games`,request);
  }
}
