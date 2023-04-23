import { Component } from '@angular/core';
import { DevelopersService } from './developers.service';
import { DevelopersResponse } from './developer.model';

@Component({
  selector: 'app-list-developers',
  templateUrl: './list-developers.component.html',
  styleUrls: ['./list-developers.component.css']
})
export class ListDevelopersComponent {
  response_developer: DevelopersResponse | null = null
  constructor(private DevelopersService: DevelopersService){ }
  ngOnInit(){
    this.DevelopersService.getAll().subscribe(res => this.response_developer = res);
  }
}
