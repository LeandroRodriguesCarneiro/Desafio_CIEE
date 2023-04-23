import { Component } from '@angular/core';
import { CreateGame, ResponseCreateGame } from '../game.model';
import { GameService } from '../game.service';
import { DevelopersResponse } from'../../developers/developer.model';
import { DevelopersService } from'../../developers/developers.service';
import { GenderResponse } from '../../gender/gender.model';
import { GenderService } from '../../gender/gender.service';

@Component({
  selector: 'app-create-game',
  templateUrl: './create-game.component.html',
  styleUrls: ['./create-game.component.css']
})
export class CreateGameComponent {
  request:CreateGame ={
    title:'',
    description:'',
    lauch_date:0,
    developer:0,
    genders:[]
  }
  response_gender: GenderResponse|null = null;
  response_developer: DevelopersResponse|null = null;
  response: ResponseCreateGame|null = null;
  constructor(private DevelopersService:DevelopersService, private GenderService:GenderService, private GameService:GameService){ }
  ngOnInit(){
    this.GenderService.getAll().subscribe(res => this.response_gender = res);
    this.DevelopersService.getAll().subscribe(res => this.response_developer = res);
  }
  save(){
    console.log(this.request)
    this.GameService.createGame(this.request).subscribe(res => {
      this.response = res;
    })
  }
  selectGender(event:any, id:number) {
    if (event.target.checked) {
      if (this.request.genders.length >= 5) {
        event.target.checked = false;
        return;
      }
      this.request.genders.push(id);
    } else {
      this.request.genders.splice(this.request.genders.indexOf(id), 1);
    }
}
}
