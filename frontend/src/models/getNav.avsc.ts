export type AvroType = GetNav;

export interface ListItem {
    active: boolean;
    url: string;
    label: string;
    icon: string;
}

export interface GetNav {
    title: string;
    listItems: ListItem[];
}
