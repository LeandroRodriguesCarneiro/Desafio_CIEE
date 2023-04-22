import { Component } from '@angular/core';
import { ListGameService } from './list-game.service';
import { Games } from './game.model';

@Component({
  selector: 'app-list-game',
  templateUrl: './list-game.component.html',
  styleUrls: ['./list-game.component.css']
})
export class ListGameComponent {

  response_game: Games;
  
  constructor(private ListGameService: ListGameService){ }
  
  ngOninit(){
    this.ListGameService.getAll().subscribe(res=>this.response_game = res)
  }
}
