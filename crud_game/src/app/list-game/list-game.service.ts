import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import {Games} from './game.model';

@Injectable({
  providedIn: 'root'
})
export class ListGameService {
  private apiUrl = 'http://localhost:5000';
  constructor(private http: HttpClient) { }
  getAll(): Observable<Games> {
    return this.http.get<Games>(`${this.apiUrl}/all?search=games`);
  }
}
