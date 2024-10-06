import * as avro from 'avsc';

import { HorizonConfig } from '../data/horizonConfig';
import { postData, postJson, getJson } from '../utils/reqs';
import { GetButton } from '../models/getButton.avsc';
import { Button } from '../components/button';
import { GetNav } from '../models/getNav.avsc';
import { Nav } from '../components/nav';

export class Components
{
    private static host: string;
    private static schemas: Record<string, avro.Type>;

    public static async Initialize(config: HorizonConfig)
    {
        this.host = config.host;
        this.schemas = {};

        const schemaData = await getJson(`${this.host}/components/getSchema`);

        schemaData.forEach((text: any) =>
        {
            const schema = JSON.parse(text);
            this.schemas[schema.name] = avro.Type.forSchema(schema);
        });
    }

    public static async CreateButton(config: GetButton): Promise<Button>
    {
        const html = await this.CreateRequest("GetButton", config);
        const element = this.CreateElement<HTMLAnchorElement>(html);

        return new Button(element);
    }

    public static async CreateNav(config: GetNav): Promise<Nav>
    {
        const html = await this.CreateRequest("GetNav", config);
        const element = this.CreateElement<HTMLDivElement>(html);

        return new Nav(element);
    }

    private static CreateElement<T extends HTMLElement>(html: string): T 
    {
        const template = document.createElement("template");
        template.innerHTML = html;

        return template.content.firstChild as T;
    }

    private static async CreateRequest(name: string, payload: object)
    {
        if (this.schemas[name] == undefined)
            return undefined;

        const buffer = this.schemas[name].toBuffer(payload);

        const response = await postData(`${this.host}/components/${this.toLowerFirst(name)}`, buffer);
        if (response == undefined)
            return undefined;

        const compResponse = this.schemas["ComponentResponse"].fromBuffer(response);
        if (compResponse == undefined)
            return undefined;

        return compResponse.html;
    }

    private static toLowerFirst(str: string)
    {
        return str.charAt(0).toLowerCase() + str.slice(1);
    }
}