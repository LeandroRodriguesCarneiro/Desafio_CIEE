import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListGameComponent } from './game/list-game.component';
import { ListGenderComponent } from './gender/list-gender.component';
import { CreateGenderComponent } from './gender/create-gender/create-gender.component'
import { ListDevelopersComponent } from './developers/list-developers.component';
import { CreateDeveloperComponent } from './developers/create-developer/create-developer.component';
import { CreateGameComponent } from './game/create-game/create-game.component';
import { UpdateGameComponent } from './game/update-game/update-game.component';


const routes: Routes = [
  {path: 'game', component: ListGameComponent},
  {path: 'game/create-game', component:CreateGameComponent},
  {path: 'game/update/:id', component:UpdateGameComponent},
  {path: 'gender', component: ListGenderComponent},
  {path: 'gender/create-gender', component: CreateGenderComponent},
  {path: 'developer', component: ListDevelopersComponent},
  {path: 'developer/create-developer', component: CreateDeveloperComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
