
export async function postJson(path: string, payload: object)
{
    try
    {
        const response = await fetch(path, {
            method: 'POST',
            headers: [
                ['Content-Type', 'application/json']
            ],
            body: JSON.stringify(payload)
        });

        if (!response.ok)
            throw new Error(`HTTP error! Status: ${response.status} ${await response.text()}`);

        return await response.json();
    }
    catch (error)
    {
        console.error(`[reqs.postJson] ${path} - `, error);
    }
}

export async function postData(path: string, payload: any): Promise<Buffer | undefined>
{
    try
    {
        const response = await fetch(path, {
            method: 'POST',
            headers: [
                ['Content-Type', 'application/octet-stream']
            ],
            body: payload
        });

        if (!response.ok)
            throw new Error(`HTTP error! Status: ${response.status} ${await response.text()}`);

        return Buffer.from((await response.arrayBuffer()));
    }
    catch (error)
    {
        console.error(`[reps.postData] ${path} - `, error);
    }
}

export async function getJson(path: string)
{
    try
    {
        const response = await fetch(path, {
            method: 'GET',
            headers: [
                ['Content-Type', 'application/json']
            ]
        });

        if (!response.ok)
            throw new Error(`HTTP error! Status: ${response.status} ${await response.text()}`);

        return await response.json();
    }
    catch (error)
    {
        console.error(`[reps.postData] ${path} - `, error);
    }
}