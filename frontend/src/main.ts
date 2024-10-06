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
                active: true,
                url: "#",
                label: "Hello",
                icon: "circle-play"
            },
            {
                active: false,
                url: "#",
                label: "Hello",
                icon: "circle-play"
            },
            {
                active: false,
                url: "#",
                label: "Hello",
                icon: "circle-play"
            }
        ]
    });

    const nav2 = await Components.CreateNav({
        title: "Test2",
        listItems: [
            {
                active: true,
                url: "#",
                label: "Hello",
                icon: "circle-play"
            },
            {
                active: false,
                url: "#",
                label: "Hello",
                icon: "circle-play"
            },
            {
                active: false,
                url: "#",
                label: "Hello",
                icon: "circle-play"
            }
        ]
    });

    const alert = await Components.CreateAlert({
        title: "Oh No",
        text: "Some text"
    });

    const input = await Components.CreateInput({
        id: "O-No",
        placeholder: "Some text"
    });



    const container = document.getElementById("sidebar");
    console.info(container);
    container?.appendChild(button.htmlElement);
    container?.appendChild(nav.htmlElement);
    container?.appendChild(nav2.htmlElement);
    container?.appendChild(alert.htmlElement);
    container?.appendChild(input.htmlElement);

}

main();
