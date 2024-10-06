import { EventType } from '../data/eventType';

export interface Element<T extends HTMLElement>
{
    htmlElement: T;
    addListener(type: EventType, callback: Function): void;
}