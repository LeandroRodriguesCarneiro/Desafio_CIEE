export interface DevelopersResponse {
    data: Developer[];
    search: string;
  }
  
export interface Developer {
  id: number;
  developer: string;
}

export interface CreateDeveloper {
  developer: string;
}

export interface CreateDeveloperResponse {
  developer: string;
  id: number;
}