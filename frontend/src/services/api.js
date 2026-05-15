const API_BASE = "http://localhost:8000/api";

export const api = {
  // Obtener todos los trámites y documentos
  obtenerDocumentos: async () => {
    const response = await fetch(`${API_BASE}/documentos/`);
    if (!response.ok) throw new Error("No se pudo conectar con Django");
    return await response.json();
  },

  // Actualizar un documento específico (por ejemplo, subir PDF)
  actualizarDocumento: async (id, formData) => {
    const response = await fetch(`${API_BASE}/documentos/${id}/`, {
      method: 'PATCH',
      body: formData,
    });
    return await response.json();
  },

  // Guardar un nuevo reporte en la base de datos
  guardarReporte: async (data) => {
    const response = await fetch(`${API_BASE}/reportes/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) throw new Error("Error al guardar el reporte en el servidor");
    return await response.json();
  },

  // Consultar el historial de reportes creados
  obtenerHistorialReportes: async () => {
    const response = await fetch(`${API_BASE}/reportes/`);
    if (!response.ok) throw new Error("No se pudo obtener el historial");
    return await response.json();
  }
};