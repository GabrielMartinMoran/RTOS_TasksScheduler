import { Component, Input, OnInit } from '@angular/core';
import { ExecutionResult } from 'src/models/execution_result';

@Component({
  selector: 'app-result-table',
  templateUrl: './result-table.component.html',
  styleUrls: ['./result-table.component.css']
})
export class ResultTableComponent implements OnInit {

  POSSIBLE_COLORS = ['#f1c5c5', '#ffeb99', '#c3aed6', '#f5b971', '#b9cced', '#e9e1cc'];
  avaliableColors = [];

  @Input() result: ExecutionResult;

  constructor() { }

  ngOnInit(): void {
    this.setProcessorsColors();
  }

  setProcessorsColors(): void {
    console.log(Object.keys(this.result?.processors).length);
    for (let i = 0; i < Object.keys(this.result?.processors).length; i++) {
      const processor = this.result.processors[i];
      processor.color = this.getRandomColor();
    }
  }

  getRandomColor(): string {
    if (this.avaliableColors.length === 0) {
      for (const color of this.POSSIBLE_COLORS) {
        this.avaliableColors.push(color);
      }
    }
    const index = Math.floor(Math.random() * this.avaliableColors.length);
    const col = this.avaliableColors[index];
    this.avaliableColors.splice(index, 1);
    return col;
  }

  getHeaders(): string[] {
    const headers = ['Procesadores'];
    for (let i = 0; i < this.result.hyperperiod; i++) {
      headers.push(i.toString());
    }
    return headers;
  }

  processorsIndexes(): number[] {
    const indexes = [];
    for (let i = 0; i < Object.keys(this.result.processors).length; i++) {
      indexes.push(i);
    }
    return indexes;
  }

  getProcessorData(index: number): string[] {
    const procData = [`Proc. ${index + 1}`];
    for (const task of this.result.processors[index]) {
      procData.push(task);
    }
    return procData;
  }

}
