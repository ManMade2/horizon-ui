import { EventType } from '../data/eventType';
import { Element } from './element';

export class Input implements Element<HTMLInputElement>
{
    htmlElement: HTMLInputElement;

    constructor(element: HTMLInputElement)
    {
        this.htmlElement = element;
    }

    addListener(type: EventType, callback: Function): void
    {
        throw new Error('Method not implemented.');
    }
}