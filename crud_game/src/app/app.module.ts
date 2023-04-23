import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ListGameComponent } from './game/list-game.component';
import { HttpClientModule } from '@angular/common/http';
import { ListGenderComponent } from './gender/list-gender.component';
import { ListDevelopersComponent } from './developers/list-developers.component';
import { CreateDeveloperComponent } from './developers/create-developer/create-developer.component';
import { FormsModule } from '@angular/forms';
import { CreateGenderComponent } from './gender/create-gender/create-gender.component';
import { CreateGameComponent } from './game/create-game/create-game.component';
import { UpdateGameComponent } from './game/update-game/update-game.component';

@NgModule({
  declarations: [
    AppComponent,
    ListGameComponent,
    ListGenderComponent,
    ListDevelopersComponent,
    CreateDeveloperComponent,
    CreateGenderComponent,
    CreateGameComponent,
    UpdateGameComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
