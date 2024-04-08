async function getData(url = "") {
    const response = await fetch(url, {
        method: "GET",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
    });

    return await response.json();
}


async function postEntity(url = "http://localhost:7777/entities/", data={}) {
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });

    return await response.json();
}


const nodes = getData("http://localhost:7777/entities_nodes/");
const edges = getData("http://localhost:7777/edges/");

var options = {
    autoResize: false,
    height: '100%',
    width: '100%',
    clickToUse: false
};

Promise.all([nodes, edges])
    .then((responses) => {
        let nd = new vis.DataSet(responses[0]);
        let ed = new vis.DataSet(responses[1]);

        var container = document.getElementById("mynetwork");
        var data = {
            nodes: nd,
            edges: ed,
        };

        var network = new vis.Network(container, data, options);

        window.addEventListener("DOMContentLoaded", function () {
            var list = document.getElementById("list");

            responses[0].foreEach((entity) => {
                const ent = document.createElement('div')
                ent.innerHTLM = entity.name;

                console.log(entity.name);

                list.appendChild(ent);
            });
        });
    });


async function renderData() {
    const nodes = await getData("http://localhost:7777/entities_nodes/");

    var list = document.getElementById("list");

    nodes.forEach((entity) => {
        const ent = document.createElement('div')
        ent.innerHTLM = entity.name;

        console.log(entity.label);

        list.appendChild(ent);
    });
}

window.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("my-form");

    document.getElementById("done").addEventListener("click", function () {
        var name = document.getElementById("name").value;
        var description = document.getElementById("description").value;

        const data = {
            name,
            description,
            image_url: null
        };

        postEntity("http://localhost:7777/entities/", data)
            .then((res) => {
                console.log(res);
                form.submit();
            });
    });
});
