import { Component, Input, OnInit } from '@angular/core';
import { AppComponent } from 'src/app/app.component';
import { Task } from 'src/models/task';

@Component({
  selector: 'app-task-card',
  templateUrl: './task-card.component.html',
  styleUrls: ['./task-card.component.css']
})
export class TaskCardComponent implements OnInit {

  @Input() task: Task;
  @Input() parent: AppComponent;

  constructor() { }

  ngOnInit(): void {
  }

  delete(): void {
    this.parent.deleteTask(this.task);
  }

}
