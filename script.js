document.addEventListener("DOMContentLoaded", function () {
    cargarDatos();
    actualizarTablas();
});

function mostrarSeccion(seccion) {
    document.querySelectorAll('.section').forEach(function (section) {
        section.style.display = 'none';
    });
    document.getElementById(seccion).style.display = 'block';
}

function mostrarFormularioPersona() {
    document.getElementById('formulario-persona').style.display = 'block';
}

function mostrarFormularioProveedor() {
    document.getElementById('formulario-proveedor').style.display = 'block';
}

function mostrarFormularioMercaderia() {
    document.getElementById('formulario-mercaderia').style.display = 'block';
    actualizarSelectProveedores();
}

function mostrarFormularioEntrada() {
    document.getElementById('formulario-entrada').style.display = 'block';
    actualizarSelectMercaderias('mercaderiaEntrada');
}

function mostrarFormularioSalida() {
    document.getElementById('formulario-salida').style.display = 'block';
    actualizarSelectMercaderias('mercaderiaSalida');
}

function actualizarSelectProveedores() {
    let proveedores = obtenerProveedores();
    let select = document.getElementById('proveedorMercaderia');
    select.innerHTML = '';
    proveedores.forEach(proveedor => {
        let option = document.createElement('option');
        option.value = proveedor.id;
        option.textContent = proveedor.nombre;
        select.appendChild(option);
    });
}

function actualizarSelectMercaderias(selectId) {
    let mercaderias = obtenerMercaderias();
    let select = document.getElementById(selectId);
    select.innerHTML = '';
    mercaderias.forEach(mercaderia => {
        let option = document.createElement('option');
        option.value = mercaderia.id;
        option.textContent = mercaderia.nombre;
        select.appendChild(option);
    });
}

function cargarDatos() {
    if (!localStorage.getItem('almacenData')) {
        localStorage.setItem('almacenData', JSON.stringify({ personas: [], proveedores: [], mercaderias: [], almacen: [] }));
    }
}

function obtenerDatos() {
    return JSON.parse(localStorage.getItem('almacenData'));
}

function guardarDatos(datos) {
    localStorage.setItem('almacenData', JSON.stringify(datos));
}

function agregarPersona() {
    let datos = obtenerDatos();
    let nuevaPersona = {
        id: datos.personas.length + 1,
        nombre: document.getElementById('nombrePersona').value,
        apellido: document.getElementById('apellidoPersona').value,
        telefono: document.getElementById('telefonoPersona').value,
        email: document.getElementById('emailPersona').value
    };
    datos.personas.push(nuevaPersona);
    guardarDatos(datos);
    actualizarTablas();
}

function agregarProveedor() {
    let datos = obtenerDatos();
    let nuevoProveedor = {
        id: datos.proveedores.length + 1,
        nombre: document.getElementById('nombreProveedor').value,
        telefono: document.getElementById('telefonoProveedor').value,
        email: document.getElementById('emailProveedor').value,
        localidad: document.getElementById('localidadProveedor').value
    };
    datos.proveedores.push(nuevoProveedor);
    guardarDatos(datos);
    actualizarTablas();
}

function agregarMercaderia() {
    let datos = obtenerDatos();
    let nuevaMercaderia = {
        id: datos.mercaderias.length + 1,
        nombre: document.getElementById('nombreMercaderia').value,
        proveedor: document.getElementById('proveedorMercaderia').value,
        detalle: document.getElementById('detalleMercaderia').value,
        fragmentacion: document.getElementById('fragmentacionMercaderia').value
    };
    datos.mercaderias.push(nuevaMercaderia);
    guardarDatos(datos);
    actualizarTablas();
}

function agregarEntrada() {
    let datos = obtenerDatos();
    let mercaderiaId = document.getElementById('mercaderiaEntrada').value;
    let cantidad = parseInt(document.getElementById('cantidadEntrada').value);
    let entrada = {
        mercaderiaId: mercaderiaId,
        cantidad: cantidad,
        fecha: new Date().toLocaleString()
    };
    datos.almacen.push(entrada);
    guardarDatos(datos);
    actualizarTablas();
}

function registrarSalida() {
    let datos = obtenerDatos();
    let mercaderiaId = document.getElementById('mercaderiaSalida').value;
    let cantidad = parseInt(document.getElementById('cantidadSalida').value);
    let mercaderia = datos.almacen.find(item => item.mercaderiaId == mercaderiaId);
    if (mercaderia && mercaderia.cantidad >= cantidad) {
        mercaderia.cantidad -= cantidad;
        guardarDatos(datos);
        actualizarTablas();
    } else {
        alert('No hay suficiente stock disponible.');
    }
}

function actualizarTablas() {
    actualizarTablaPersonas();
    actualizarTablaProveedores();
    actualizarTablaMercaderias();
    actualizarTablaAlmacen();
}

function actualizarTablaPersonas() {
    let datos = obtenerDatos();
    let tabla = document.getElementById('tablaPersonas');
    tabla.innerHTML = `<tr>
        <th>ID</th>
        <th>Nombre</th>
        <th>Apellido</th>
        <th>Teléfono</th>
        <th>Email</th>
    </tr>`;
    datos.personas.forEach(persona => {
        let row = tabla.insertRow();
        row.insertCell(0).textContent = persona.id;
        row.insertCell(1).textContent = persona.nombre;
        row.insertCell(2).textContent = persona.apellido;
        row.insertCell(3).textContent = persona.telefono;
        row.insertCell(4).textContent = persona.email;
    });
}

function actualizarTablaProveedores() {
    let datos = obtenerDatos();
    let tabla = document.getElementById('tablaProveedores');
    tabla.innerHTML = `<tr>
        <th>ID</th>
        <th>Nombre</th>
        <th>Teléfono</th>
        <th>Email</th>
        <th>Localidad</th>
    </tr>`;
    datos.proveedores.forEach(proveedor => {
        let row = tabla.insertRow();
        row.insertCell(0).textContent = proveedor.id;
        row.insertCell(1).textContent = proveedor.nombre;
        row.insertCell(2).textContent = proveedor.telefono;
        row.insertCell(3).textContent = proveedor.email;
        row.insertCell(4).textContent = proveedor.localidad;
    });
}

function actualizarTablaMercaderias() {
    let datos = obtenerDatos();
    let tabla = document.getElementById('tablaMercaderias');
    tabla.innerHTML = `<tr>
        <th>ID</th>
        <th>Nombre</th>
        <th>Proveedor</th>
        <th>Detalle</th>
        <th>Fragmentación</th>
    </tr>`;
    datos.mercaderias.forEach(mercaderia => {
        let row = tabla.insertRow();
        row.insertCell(0).textContent = mercaderia.id;
        row.insertCell(1).textContent = mercaderia.nombre;
        row.insertCell(2).textContent = obtenerProveedorNombre(mercaderia.proveedor);
        row.insertCell(3).textContent = mercaderia.detalle;
        row.insertCell(4).textContent = mercaderia.fragmentacion;
    });
}

function actualizarTablaAlmacen() {
    let datos = obtenerDatos();
    let tabla = document.getElementById('tablaAlmacen');
    tabla.innerHTML = `<tr>
        <th>ID Mercadería</th>
        <th>Nombre</th>
        <th>Cantidad</th>
        <th>Fecha de Entrada</th>
    </tr>`;
    datos.almacen.forEach(item => {
        let mercaderia = datos.mercaderias.find(m => m.id == item.mercaderiaId);
        let row = tabla.insertRow();
        row.insertCell(0).textContent = item.mercaderiaId;
        row.insertCell(1).textContent = mercaderia ? mercaderia.nombre : 'Desconocido';
        row.insertCell(2).textContent = item.cantidad;
        row.insertCell(3).textContent = item.fecha;
    });
}

function obtenerProveedores() {
    let datos = obtenerDatos();
    return datos.proveedores;
}

function obtenerMercaderias() {
    let datos = obtenerDatos();
    return datos.mercaderias;
}

function obtenerProveedorNombre(id) {
    let proveedores = obtenerProveedores();
    let proveedor = proveedores.find(p => p.id == id);
    return proveedor ? proveedor.nombre : 'Desconocido';
}
