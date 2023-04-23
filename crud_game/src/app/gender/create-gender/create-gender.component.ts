import { Component } from '@angular/core';
import { CreateGender, CreateGenderResponse } from '../gender.model';
import { GenderService } from '../gender.service';

@Component({
  selector: 'app-create-gender',
  templateUrl: './create-gender.component.html',
  styleUrls: ['./create-gender.component.css']
})
export class CreateGenderComponent {
  request: CreateGender = {
    gender: ''
  };
  response: CreateGenderResponse | null = null;

  constructor(private genderService: GenderService) { }

  save() {
    this.genderService.createGender(this.request).subscribe(res => {
      this.response = res;
    });
  }
}
