import { Component } from '@angular/core';
import { Planner } from 'src/models/planner';
import { Scheduler } from 'src/models/scheduler';
import { Task } from 'src/models/task';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  MIN_PROCESSORS = 1;
  MAX_PROCESSORS = 50;

  PLANNERS: Planner[] = [
    {
      name: 'Ejecutivo cíclico',
      value: 'cyclicExecutive',
      maxProcessors: 1
    },
    {
      name: 'Rate monotonic',
      value: 'rateMonotonic',
      maxProcessors: -1
    }
  ];

  selectedPlanner: Planner = this.PLANNERS[0];
  scheduler: Scheduler;

  constructor() {
    this.scheduler = new Scheduler();
    this.scheduler.planner = this.selectedPlanner.value;
  }

  schedule(): void {
    console.log(this.scheduler);
  }

  onPlannerChange(planner: any): void {
    this.scheduler.planner = planner.value;
    if (planner.maxProcessors > 0) {
      this.scheduler.processors = planner.maxProcessors;
    }
  }

  canChangeProcessors(): boolean {
    return this.selectedPlanner.maxProcessors === -1;
  }

  addTask(): void {
    const task = new Task();
    task.name = `T${this.scheduler.tasks.length + 1}`;
    this.scheduler.tasks.push(task);
  }

  deleteTask(task: Task): void {
    this.scheduler.tasks.splice(this.scheduler.tasks.indexOf(task), 1);
  }

}
