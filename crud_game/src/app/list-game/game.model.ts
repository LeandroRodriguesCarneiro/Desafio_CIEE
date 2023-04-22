    export interface Game {
    title: string;
    description: string;
    releaseYear: number;
    developer: string;
    genres: string[];
    }
    
    export interface Games {
    [id: string]: Game;
    }