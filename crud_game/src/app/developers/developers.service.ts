import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { CreateDeveloper, DevelopersResponse,CreateDeveloperResponse } from "./developer.model";


@Injectable({
  providedIn: 'root'
})
export class DevelopersService {
  private apiUrl = 'http://localhost:5000';
  constructor(private http: HttpClient) { }
  getAll(): Observable<DevelopersResponse> {
    return this.http.get<DevelopersResponse>(`${this.apiUrl}/all?search=developer`);
  }
  createDeveloper(request: CreateDeveloper): Observable<CreateDeveloperResponse>{
    return this.http.post<CreateDeveloperResponse>(`${this.apiUrl}/add?search=developer`,request);
  }
}
