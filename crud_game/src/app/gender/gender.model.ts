export interface Gender {
    gender: string;
    id: number;
}
    
export interface GenderResponse {
    data: Gender[];
    search: string;
}

export interface CreateGender{
    gender: string;
}

export interface CreateGenderResponse {
    id: number;
    gender: string;
}