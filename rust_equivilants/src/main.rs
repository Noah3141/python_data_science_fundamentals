use plotters::prelude::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create a new drawing area with a bitmap backend
    let root = BitMapBackend::new("3d_plot.png", (800, 600)).into_drawing_area();

    // Clear the drawing area with a white background
    root.fill(&WHITE)?;

    // Create a new 3D chart
    let mut chart = ChartBuilder::on(&root)
        .margin(40)
        .caption("3D Plot", ("sans-serif", 30))
        .build_cartesian_3d(-5.0..5.0, -5.0..5.0, -5.0..5.0)?;

    // Configure the axes
    chart.configure_axes().draw()?;

    // Generate data for the 3D plot
    let mut data = Vec::new();
    for x in -50..50 {
        for y in -50..50 {
            let x_val = (x as f64) / 10.0;
            let y_val = (y as f64) / 10.0;
            let z_val = (x_val * x_val + y_val * y_val).sqrt();

            data.push((x_val, y_val, z_val));
        }
    }

    // Create a 3D line series from the data and draw it
    chart.draw_series(
        SurfaceSeries::grid(data, 100, 100, |(x, y, z)| *z)
            .style(&plotters::style::GradientStyle::Vertical)
    )?;

    // Save the chart to a PNG file
    chart.present()?;
    Ok(())
}
