import './Card.css'

export default function Card({ title, value, subtitle, children }) {
  return (
    <div className="card">
      {title && <h3 className="card-title">{title}</h3>}
      {value && <div className="card-value">{value}</div>}
      {subtitle && <p className="card-subtitle">{subtitle}</p>}
      {children}
    </div>
  )
}
