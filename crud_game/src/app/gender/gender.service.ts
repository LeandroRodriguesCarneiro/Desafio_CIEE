import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { CreateGender, GenderResponse, CreateGenderResponse } from "./gender.model";

@Injectable({
  providedIn: 'root'
})
export class GenderService {
  private apiUrl = 'http://localhost:5000';
  constructor(private http: HttpClient) { }
  getAll(): Observable<GenderResponse> {
    return this.http.get<GenderResponse>(`${this.apiUrl}/all?search=gender`);
  }
  createGender(request: CreateGender): Observable<CreateGenderResponse>{
    return this.http.post<CreateGenderResponse>(`${this.apiUrl}/add?search=gender`,request);
  }
}
