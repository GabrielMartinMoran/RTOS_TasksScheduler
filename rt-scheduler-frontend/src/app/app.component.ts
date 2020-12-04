import { Component } from '@angular/core';
import { ExecutionResult } from 'src/models/execution_result';
import { Planner } from 'src/models/planner';
import { Scheduler } from 'src/models/scheduler';
import { Task } from 'src/models/task';
import { SchedulerService } from './services/scheduler.service';
import Swal from 'sweetalert2/dist/sweetalert2.js';
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
      name: 'Ejecutivo cíclico (FIFO)',
      value: 'CYCLIC_EXECUTIVE',
      maxProcessors: 1
    },
    {
      name: 'Rate monotonic',
      value: 'RATE_MONOTONIC',
      maxProcessors: -1
    }
  ];

  selectedPlanner: Planner = this.PLANNERS[0];
  scheduler: Scheduler;
  result: ExecutionResult = null;

  constructor(private schedulerService: SchedulerService) {
    this.scheduler = new Scheduler();
    this.scheduler.planner = this.selectedPlanner.value;
  }

  schedule(): void {
    this.result = null;
    this.schedulerService.schedule(this.scheduler).subscribe((res) => {
      this.result = res;
    }, (err) => {
      console.log(err);
      let message = 'El schedule no pudo realizarse.';
      if (err.error.message) {
        message += '<br><b>' + err.error.message + '</b>';
      }
      Swal.fire('Scheduler', message, 'error');
    });
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

  validParameters(): boolean {
    return (this.scheduler.tasks.length > 0) && !!this.scheduler.planner;
  }

}
