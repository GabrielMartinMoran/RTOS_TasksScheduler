import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Scheduler } from 'src/models/scheduler';

@Injectable({
    providedIn: 'root'
})
export class SchedulerService {

    ENDPOINT = 'http://localhost:5000/api';

    constructor(private http: HttpClient) {
    }

    public schedule(data: Scheduler): Observable<any> {
        return this.http.post(`${this.ENDPOINT}/schedule`, data);
    }
}
