import { Component } from '@angular/core';
import { GameService } from '../game.service';
import { DevelopersResponse } from'../../developers/developer.model';
import { DevelopersService } from'../../developers/developers.service';
import { GenderResponse } from '../../gender/gender.model';
import { GenderService } from '../../gender/gender.service';
import { ActivatedRoute } from '@angular/router';
import { CreateGame } from '../game.model';

@Component({
  selector: 'app-update-game',
  templateUrl: './update-game.component.html',
  styleUrls: ['./update-game.component.css']
})
export class UpdateGameComponent {

  id:string|null =null;
  response_gender: GenderResponse|null = null;
  response_developer: DevelopersResponse|null = null;
  request: CreateGame|null = null
  genders_list: number[] = [];
  id_developer: number=0;
  constructor(private DevelopersService:DevelopersService, private GenderService:GenderService, private GameService:GameService,private rout:ActivatedRoute){}
  ngOnInit(){
    this.id = this.rout.snapshot.paramMap.get('id');
    this.GenderService.getAll().subscribe(res => this.response_gender = res);
    this.DevelopersService.getAll().subscribe(res => this.response_developer = res);
    if (this.id !== null) {
      this.GameService.getGame(this.id).subscribe(res => {
        this.genders_list = res.data.genders.map(str=>Number(str))
        if(this.response_developer && this.response_developer.data){
          for(let i = 0;i<this.response_developer.data.length;i++){
            if(this.response_developer.data[i].developer == res.data.developer){
              this.id_developer = this.response_developer.data[i].id
            }
          }
        }
        if(this.response_gender){
          for(let i=0;i<this.response_gender.data.length;i++){
            for(let j=0;j<res.data.genders.length;j++){
              if(this.response_gender.data[i].gender===res.data.genders[j]){
                this.genders_list.push(this.response_gender.data[i].id)
              }
            }
          }
        }
        this.genders_list = this.genders_list.filter(x => !isNaN(x));
        this.request={
          title: res.data.title,
          description: res.data.description,
          lauch_date: res.data.year,
          developer: this.id_developer,
          genders: this.genders_list
        }
      });
    }
  }
  updateGenders(event: any, id: any) {
    if(this.request){
      const maxSelections = 5;
      const numSelections = this.request.genders.length;
    
      if (numSelections >= maxSelections && !event.target.checked) {
        return;
      }
    
      if (event.target.checked) {
        this.request.genders.push(id);
      } else {
        const index = this.request.genders.indexOf(id);
        if (index !== -1) {
          this.request.genders.splice(index, 1);
        }
      }
  }
  
    console.log(this.request.genders);
  }
  
  
  
  
  update(){
    console.log(this.request)
  }
}
