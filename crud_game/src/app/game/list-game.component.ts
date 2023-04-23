import { Component } from '@angular/core';
import { GameService } from './game.service';
import { GamesResponse } from './game.model';

@Component({
  selector: 'app-list-game',
  templateUrl: './list-game.component.html',
  styleUrls: ['./list-game.component.css']
})
export class ListGameComponent {
  
  response_games: GamesResponse | null = null;  

  constructor(private GameService: GameService){
    
   }
  
  ngOnInit(){
    this.GameService.getAll().subscribe(res => this.response_games = res);
  }
}