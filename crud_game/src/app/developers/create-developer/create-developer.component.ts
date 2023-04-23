import { Component } from '@angular/core';
import { CreateDeveloper,CreateDeveloperResponse } from '../developer.model'
import { DevelopersService } from '../developers.service';

@Component({
  selector: 'app-create-developer',
  templateUrl: './create-developer.component.html',
  styleUrls: ['./create-developer.component.css']
})
export class CreateDeveloperComponent {
  request: CreateDeveloper ={
    developer: ""
  }
  response: CreateDeveloperResponse| null = null
  constructor(private DevelopersService: DevelopersService){ }
  save(){
    this.DevelopersService.createDeveloper(this.request).subscribe(res => {
      this.response = res;
    });
  }
}
