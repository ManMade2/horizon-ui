import { EventType } from '../data/eventType';
import { Element } from './element';

export class Button implements Element<HTMLAnchorElement>
{
    htmlElement: HTMLAnchorElement;

    constructor(element: HTMLAnchorElement)
    {
        this.htmlElement = element;
    }

    addListener(type: EventType, callback: Function): void
    {
        throw new Error('Method not implemented.');
    }
}