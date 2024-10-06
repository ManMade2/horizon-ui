import { EventType } from '../data/eventType';
import { Element } from './element';

export class Alert implements Element<HTMLDivElement>
{
    htmlElement: HTMLDivElement;

    constructor(element: HTMLDivElement)
    {
        this.htmlElement = element;
    }

    addListener(type: EventType, callback: Function): void
    {
        throw new Error('Method not implemented.');
    }
}