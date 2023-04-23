import { Component } from '@angular/core';
import {GenderService} from './gender.service'
import { GenderResponse } from './gender.model';

@Component({
  selector: 'app-list-gender',
  templateUrl: './list-gender.component.html',
  styleUrls: ['./list-gender.component.css']
})
export class ListGenderComponent {
  response_gender: GenderResponse | null = null;  

  constructor(private GenderService: GenderService){
    
   }
  
  ngOnInit(){
    this.GenderService.getAll().subscribe(res => this.response_gender = res);
  }
}