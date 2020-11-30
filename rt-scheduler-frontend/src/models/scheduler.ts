import { Task } from './task';

export class Scheduler {
    planner: string;
    processors: number;
    tasks: Task[];

    constructor() {
        this.processors = 1;
        this.tasks = [];
    }
}