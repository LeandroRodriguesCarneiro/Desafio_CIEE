export interface Game {
    id: number;
    title: string;
    description: string;
    developer: string;
    year: number;
    genders: string[];
  }
  
export interface GamesResponse {
  data: Game[];
  search: string;
}

export interface CreateGame {
  title: string;
  description: string;
  lauch_date: number;
  developer: number;
  genders: number[];
}

export interface ResponseCreateGame {
  id: number;
  title: string;
  description: string;
  year: number;
  developer: string;
  genders: string[];
}

export interface GameResponse {
  search: string;
  data: Game;
}