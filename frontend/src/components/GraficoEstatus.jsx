import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

export const GraficoEstatus = ({ documentos }) => {
  const conteo = {
    rojo: documentos.filter(d => d.semaforo_dinamico === 'rojo').length,
    amarillo: documentos.filter(d => d.semaforo_dinamico === 'amarillo').length,
    verde: documentos.filter(d => d.semaforo_dinamico === 'verde').length,
  };

  const data = {
    labels: ['Crítico', 'Próximo', 'Vigente'],
    datasets: [{
      data: [conteo.rojo, conteo.amarillo, conteo.verde],
      backgroundColor: ['#ffcccc', '#fff3cd', '#d4edda'],
      borderColor: ['red', '#856404', 'green'],
      borderWidth: 1,
    }],
  };

  return (
    <div style={{ width: '300px', margin: '20px auto' }}>
      <Pie data={data} />
    </div>
  );
};