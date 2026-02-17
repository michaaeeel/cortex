import Card from '../components/ui/Card'

export default function Settings() {
  return (
    <div>
      <h1 className="page-title">Settings</h1>
      <Card>
        <h3 style={{ marginBottom: 16 }}>Profile</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12, maxWidth: 400 }}>
          <label style={{ fontSize: '0.85rem', color: 'var(--color-text-muted)' }}>
            Username
            <input
              type="text"
              disabled
              placeholder="username"
              style={{
                display: 'block',
                width: '100%',
                marginTop: 4,
                padding: '8px 12px',
                border: '1px solid var(--color-border)',
                borderRadius: 'var(--radius)',
                backgroundColor: 'var(--color-bg)',
              }}
            />
          </label>
          <label style={{ fontSize: '0.85rem', color: 'var(--color-text-muted)' }}>
            Organization
            <input
              type="text"
              placeholder="Your organization"
              style={{
                display: 'block',
                width: '100%',
                marginTop: 4,
                padding: '8px 12px',
                border: '1px solid var(--color-border)',
                borderRadius: 'var(--radius)',
              }}
            />
          </label>
          <button className="btn-primary" style={{ alignSelf: 'flex-start', marginTop: 8 }}>
            Save Changes
          </button>
        </div>
      </Card>
    </div>
  )
}
