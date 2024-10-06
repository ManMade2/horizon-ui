import './styles/main.css';

import { Components } from './scripts/components';

async function main()
{
    await Components.Initialize({ host: "http://127.0.0.1:5000/api/v1" });
    const button = await Components.CreateButton({
        id: 'test',
        label: 'Click Me',
        css_class: 'horizonButton',
        url: ''
    });


    const nav = await Components.CreateNav({
        title: "Test",
        listItems: [
            {
                active: false,
                url: "#",
                label: "Hello",
                icon: "circle-play"
            }
        ]
    });

    const container = document.getElementById("sidebar");
    console.info(container);
    container?.appendChild(button.htmlElement);
    container?.appendChild(nav.htmlElement);
}

main();
